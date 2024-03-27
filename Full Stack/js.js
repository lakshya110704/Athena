document.addEventListener('DOMContentLoaded', function() { 
    const usersIcon = document.getElementById('users-icon'); 
    const languageIcon = document.getElementById('language-icon'); 
    const fileIcon = document.getElementById('file-icon'); 
    const usersDropdown = document.getElementById('users-dropdown'); 
    const languageDropdown = document.getElementById('language-dropdown'); 
    const fileDropdown = document.getElementById('file-dropdown'); 

    usersIcon.addEventListener('mouseover', function() { 
        usersDropdown.style.display = 'block'; 
    }); 

    usersIcon.addEventListener('mouseout', function() { 
        usersDropdown.style.display = 'none'; 
    }); 

    languageIcon.addEventListener('mouseover', function() { 
        languageDropdown.style.display = 'block'; 
    }); 

    languageIcon.addEventListener('mouseout', function() { 
        languageDropdown.style.display = 'none'; 
    }); 

    fileIcon.addEventListener('mouseover', function() { 
        fileDropdown.style.display = 'block'; 
    }); 

    fileIcon.addEventListener('mouseout', function() { 
        fileDropdown.style.display = 'none'; 
    }); 

    document.addEventListener('DOMContentLoaded', function() { 
        const dropdownLinks = document.querySelectorAll('.dropdown-content a'); 
        
        dropdownLinks.forEach(function(link) {
            link.addEventListener('click', function(e) {
                e.preventDefault(); // Prevent the default behavior of the link
                
                // Get the URL to navigate to
                const url = this.getAttribute('href');
                
                // Navigate to the URL
                window.location.href = url;
            });
        });
    });
    
});

