/**
 * Chat functionality for the Agricultural Assistant
 */

document.addEventListener('DOMContentLoaded', function() {
    const chatMessages = document.getElementById('chat-messages');
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const exampleQuestions = document.querySelectorAll('.question-link');
    
    // Store chat history
    let chatHistory = [];
    
    // Initialize chat
    initChat();
    
    // Handle form submission
    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const message = userInput.value.trim();
        if (message.length === 0) return;
        
        // Add user message to chat
        addMessage(message, 'user');
        
        // Clear input
        userInput.value = '';
        
        // Get bot response
        getBotResponse(message);
    });
    
    // Handle example question clicks
    exampleQuestions.forEach(question => {
        question.addEventListener('click', function(e) {
            e.preventDefault();
            
            const questionText = this.textContent;
            userInput.value = questionText;
            
            // Trigger form submission
            const event = new Event('submit', {
                'bubbles': true,
                'cancelable': true
            });
            chatForm.dispatchEvent(event);
        });
    });
    
    /**
     * Initialize chat elements and welcome message
     */
    function initChat() {
        // Scroll to bottom of chat
        scrollToBottom();
    }
    
    /**
     * Add a message to the chat
     * @param {string} text - Message text
     * @param {string} sender - Message sender ('user' or 'bot')
     */
    function addMessage(text, sender) {
        // Clean up old messages if chat gets too long (keep last 15 messages visible)
        const existingMessages = chatMessages.querySelectorAll('.message');
        if (existingMessages.length > 15) {
            for (let i = 0; i < existingMessages.length - 15; i++) {
                existingMessages[i].remove();
            }
        }
        
        // Create message element
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        // Create content element
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        // Process the text for better display - no truncation to allow full responses
        contentDiv.innerHTML = convertMarkdownToHtml(text);
        
        // Create time element
        const timeDiv = document.createElement('div');
        timeDiv.className = 'message-time';
        timeDiv.textContent = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
        
        // Assemble message
        messageDiv.appendChild(contentDiv);
        messageDiv.appendChild(timeDiv);
        
        // Add to chat
        chatMessages.appendChild(messageDiv);
        
        // Apply fade-in animation
        messageDiv.style.opacity = '0';
        messageDiv.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            messageDiv.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
            messageDiv.style.opacity = '1';
            messageDiv.style.transform = 'translateY(0)';
        }, 10);
        
        // Scroll to bottom with delay to ensure content is rendered
        setTimeout(() => {
            scrollToBottom();
        }, 100);
        
        // Update chat history
        if (sender === 'user') {
            chatHistory.push({ role: 'user', content: text });
        } else {
            chatHistory.push({ role: 'assistant', content: text });
        }
    }
    
    /**
     * Get response from the bot
     * @param {string} message - User message
     */
    function getBotResponse(message) {
        // Show typing indicator
        showTypingIndicator();
        
        // Send message to AI
        fetch('/chat_with_bot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message
            })
        })
        .then(response => response.json())
        .then(data => {
            // Remove typing indicator
            removeTypingIndicator();
            
            if (data.success) {
                // Add bot response to chat with proper formatting
                addMessage(data.response, 'bot');
                
                // Limit client-side history to prevent memory issues
                if (chatHistory.length > 10) {
                    chatHistory = chatHistory.slice(-10);
                }
            } else {
                // Show error message from server or generic error
                const errorMsg = data.error || 'Sorry, I encountered an error. Please try again later.';
                addMessage(errorMsg, 'bot');
                console.error('Error:', data.error);
            }
        })
        .catch(error => {
            // Remove typing indicator
            removeTypingIndicator();
            
            // Show error
            addMessage('Sorry, I encountered a connection error. Please check your internet and try again.', 'bot');
            console.error('Network Error:', error);
        });
    }
    
    /**
     * Show typing indicator in chat
     */
    function showTypingIndicator() {
        // Create typing indicator
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message typing-indicator';
        typingDiv.id = 'typing-indicator';
        
        // Create typing animation
        const dotContainer = document.createElement('div');
        dotContainer.className = 'typing-dots';
        
        for (let i = 0; i < 3; i++) {
            const dot = document.createElement('span');
            dot.className = 'dot';
            dotContainer.appendChild(dot);
        }
        
        // Add to message
        typingDiv.appendChild(dotContainer);
        
        // Add to chat
        chatMessages.appendChild(typingDiv);
        
        // Scroll to bottom
        scrollToBottom();
    }
    
    /**
     * Remove typing indicator from chat
     */
    function removeTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
    
    /**
     * Scroll chat to bottom
     */
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    /**
     * Convert markdown to HTML
     * @param {string} text - Markdown text
     * @returns {string} - HTML
     */
    function convertMarkdownToHtml(text) {
        // Simple markdown to HTML conversion
        // Bold
        text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        
        // Italic
        text = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
        
        // Links
        text = text.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank">$1</a>');
        
        // Lists
        text = text.replace(/^\s*-\s+(.*?)$/gm, '<li>$1</li>');
        text = text.replace(/(<li>.*?<\/li>)/gs, '<ul>$1</ul>');
        
        // Headings
        text = text.replace(/^# (.*?)$/gm, '<h4>$1</h4>');
        text = text.replace(/^## (.*?)$/gm, '<h5>$1</h5>');
        
        // Line breaks
        text = text.replace(/\n/g, '<br>');
        
        return text;
    }
});

// Add custom styles for typing indicator
document.head.insertAdjacentHTML('beforeend', `
<style>
.typing-indicator {
    padding-bottom: 1.5rem;
}

.typing-dots {
    display: flex;
    justify-content: flex-start;
    padding: 0.5rem 0;
}

.dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: #999;
    margin-right: 4px;
    animation: dot-pulse 1.5s infinite ease-in-out;
}

.dot:nth-child(1) {
    animation-delay: 0s;
}

.dot:nth-child(2) {
    animation-delay: 0.2s;
}

.dot:nth-child(3) {
    animation-delay: 0.4s;
}

@keyframes dot-pulse {
    0%, 100% {
        transform: scale(1);
        opacity: 0.5;
    }
    50% {
        transform: scale(1.5);
        opacity: 1;
    }
}
</style>
`);
