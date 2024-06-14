// Get the file input element
const fileInput = document.getElementById('fileInput');

// Get the image preview element
const imagePreview = document.getElementById('uploadImage');

// Add event listener for file input change
fileInput.addEventListener('change', function() {
    const file = this.files[0];

    // Check if file is an image
    if (file && file.type.startsWith('image')) {
        const reader = new FileReader();

        // Read the image file as a data URL
        reader.readAsDataURL(file);

        // When loaded, set the image preview source
        reader.onload = function() {
            imagePreview.src = reader.result;
            imagePreview.style.display = 'block'; // Show the image preview
        };
    }
});
