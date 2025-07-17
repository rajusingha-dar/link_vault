document.addEventListener('DOMContentLoaded', () => {
    // Add a confirmation dialog for all delete buttons
    const deleteButtons = document.querySelectorAll('.delete-btn');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            // Prevent the link from being followed immediately
            event.preventDefault(); 
            
            const userConfirmed = confirm('Are you sure you want to delete this link?');
            
            if (userConfirmed) {
                // If confirmed, navigate to the delete link
                window.location.href = this.href;
            }
            // If not confirmed, do nothing
        });
    });

    console.log('LinkVault UI is ready!');
});
