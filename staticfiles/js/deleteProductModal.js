// Get the modal snippet
const modal = document.getElementById("deleteModal");

var productIdClicked = -1;



// Get all the delete buttons from the page
const deleteButtons = document.querySelectorAll("[id='deleteProductBtn']");

// Add the deleteConfirmation function to each delete button
deleteButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {

        // Show it and make it modal
        modal.style.display = "block";
    
        productIdClicked = button.getAttribute("data-product-id");
    })

});

// Close modal when the user clicks anywhere outside of the modal window
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Get the close and cancel confirmation window's buttons 
const closeConfirmationButton = document.getElementById("close-confirmation-btn")
const cancelConfirmationButton = document.getElementById("cancel-confirmation-btn")
closeConfirmationButton.addEventListener('click', closeConfirmationWindow);
cancelConfirmationButton.addEventListener('click', closeConfirmationWindow);

function closeConfirmationWindow() {
    modal.style.display = "none";
}


const deleteAnchor = document.getElementById("deleteConfirm");

deleteAnchor.addEventListener('click', deleteProduct);

async function deleteProduct() {
    const deleteView = 'delete/' + productIdClicked;
    modal.style.display = "none";
    await fetch(deleteView);
    window.location.reload();
}