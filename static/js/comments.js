/* global bootstrap */
const edit = document.getElementsByClassName("edit-button");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("comment-form");
const submitButton = document.getElementById("submit-update");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("delete-button");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Allows editing of comment.
* 
* When the `edit` button is clicked:
* - The associated comment's ID is retrieved.
* - The content of the corresponding comment is retrieved.
* - Populates the `commentText` textarea with the comment's content.
* - Updates the submit button to "Update".
*/
for (let button of edit) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("data-comment-id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.focus();
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

/**
* Allows deletion of comment.
* 
* Whem the delete button is clicked:
* - The associated comment's ID is retrieved.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("data-comment-id");
      deleteConfirm.href = `delete_comment/${commentId}`;
      deleteModal.show();
    });
  }