document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('login').addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Get the form data
        const formData = new FormData(this);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        // Convert data object to query parameters
        const queryParams = new URLSearchParams({
            userName: data.username,
            password: data.password
        }).toString();

        try {

            const response = await fetch(`http://localhost:8080/users/login?${queryParams}`, {
                method: 'GET',
                mode: 'no-cors',
                headers: {
                    'Content-Type': 'application/json',
                }
            });

            const result = response;
            
            //await response.json();

            const responseVar = result;

            // Display or use the stored response as needed
            console.log(responseVar);

        } catch (error) {
            console.error('Error:', error);
        }
    });
});