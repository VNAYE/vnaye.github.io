document.addEventListener("DOMContentLoaded", () => {
    const navLinks = document.querySelectorAll(".nav-links li a");
    const sections = document.querySelectorAll("section");

    const menuToggle = document.querySelector(".menu-toggle");
    const navLinksContainer = document.querySelector(".nav-links");

    menuToggle.addEventListener("click", () => {
        navLinksContainer.classList.toggle("active");
        menuToggle.classList.toggle("open"); // Add class for animation

        // Add names to social links when menu is active
        if (navLinksContainer.classList.contains("active")) {
            const socialLinks = navLinksContainer.querySelectorAll("li a i");
            socialLinks.forEach((icon) => {
                const parent = icon.parentElement;
                if (!parent.querySelector("span")) {
                    const name = {
                        "bi-github": "GitHub",
                        "bi-linkedin": "LinkedIn",
                        "bi-instagram": "Instagram",
                    }[icon.classList[1]];
                    if (name) {
                        const span = document.createElement("span");
                        span.textContent = ` ${name}`;
                        span.style.marginLeft = "5px";
                        span.style.fontSize = "0.9rem"; // Adjust font size for smaller screens
                        parent.appendChild(span);
                    }
                }
            });
        } else {
            // Remove names when menu is closed
            const spans = navLinksContainer.querySelectorAll("li a span");
            spans.forEach((span) => span.remove());
        }
    });

    // Close sidebar when clicking outside
    document.addEventListener("click", (event) => {
        if (!menuToggle.contains(event.target) && !navLinksContainer.contains(event.target)) {
            navLinksContainer.classList.remove("active");
            menuToggle.classList.remove("open");

            // Remove names when menu is closed
            const spans = navLinksContainer.querySelectorAll("li a span");
            spans.forEach((span) => span.remove());
        }
    });

    window.addEventListener("scroll", () => {
        let current = "";
        sections.forEach((section) => {
            const sectionTop = section.offsetTop - 50;
            if (pageYOffset >= sectionTop) {
                current = section.getAttribute("id");
            }
        });

        navLinks.forEach((link) => {
            link.classList.remove("active");
            if (link.getAttribute("href").includes(current)) {
                link.classList.add("active");
            }
        });
    });
});
