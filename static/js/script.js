document.addEventListener("DOMContentLoaded", () => {

    const feedbackForm = document.querySelector("form");

    if (!feedbackForm) return;

    feedbackForm.addEventListener("submit", (e) => {
        const name = feedbackForm.name?.value.trim();
        const email = feedbackForm.email?.value.trim();
        const rating = feedbackForm.rating?.value;

        if (name && name.length < 3) {
            alert("Name must be at least 3 characters");
            e.preventDefault();
            return;
        }

        if (email && !email.includes("@")) {
            alert("Please enter a valid email");
            e.preventDefault();
            return;
        }

        if (rating === "") {
            alert("Please select a rating");
            e.preventDefault();
        }
    });
});
