const medicalImage = document.getElementById("medicalImage");
const imagePreviewPopup = document.getElementById("imagePreviewPopup");
const previewImage = document.getElementById("previewImage");
const confirmImage = document.getElementById("confirmImage");
const closePreview = document.getElementById("closePreview");
let selectedFile = null;

medicalImage.addEventListener("change", function () {
    selectedFile = medicalImage.files[0];
    const imageURL = URL.createObjectURL(selectedFile);
    previewImage.src = imageURL;
    imagePreviewPopup.style.display = "flex";
});

closePreview.addEventListener("click", function () {
    imagePreviewPopup.style.display = "none";
});

confirmImage.addEventListener("click", function () {
    console.log("Image confirmed!");
    const formData = new FormData();
    formData.append("image", selectedFile);

    fetch("/analyze", {
        method: "POST",
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        console.log(data);
    });

});