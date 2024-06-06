// Get the modal
const modal = document.getElementById("deleteModal");

// Get the button that opens the modal
const deleteBtn = document.querySelectorAll("[id='deleteProductBtn']");

// Get the button element that closes the modal
const closeBtn = document.getElementById("close-confirmation-btn");

// Get the button that confirms deletion of the product
const confirmDeleteBtn = document.getElementById("deleteConfirm");

// When the user clicks the button, open the modal 
deleteBtn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on the close button, close the modal
closeBtn.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close the modal
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// When the user clicks the delete button the product is deleted
confirmDeleteBtn.onclick = function() {
    deleteConfirm.href = `delete_product/${product.Id}`;
    alert("Item deleted.");
    modal.style.display = "none";
}
