(() => {
    "use strict";

    const STORAGE_KEY = "cineverse-theme";
    const DEFAULT_THEME = "white";
    const THEMES = ["white", "dark"];

    function normalizeTheme(theme) {
        return THEMES.includes(theme) ? theme : DEFAULT_THEME;
    }

    function saveTheme(theme) {
        localStorage.setItem(STORAGE_KEY, theme);
    }

    function loadTheme() {
        return normalizeTheme(localStorage.getItem(STORAGE_KEY));
    }

    function updateButtons(theme) {
        document.querySelectorAll("[data-theme-choice]").forEach(button => {
            const active = button.dataset.themeChoice === theme;

            button.classList.toggle("is-active", active);
            button.setAttribute("aria-pressed", active);
        });
    }

    function applyTheme(theme) {
        theme = normalizeTheme(theme);

        document.documentElement.setAttribute("data-theme", theme);
        document.body.setAttribute("data-theme", theme);

        document.documentElement.classList.toggle("theme-dark", theme === "dark");
        document.documentElement.classList.toggle("theme-white", theme === "white");

        document.body.classList.toggle("theme-dark", theme === "dark");
        document.body.classList.toggle("theme-white", theme === "white");

        saveTheme(theme);
        updateButtons(theme);
    }

    function bindButtons() {
        document.querySelectorAll("[data-theme-choice]").forEach(button => {

            button.removeEventListener("click", button.__themeHandler);

            button.__themeHandler = function () {
                applyTheme(button.dataset.themeChoice);
            };

            button.addEventListener("click", button.__themeHandler);
        });
    }

    window.CineVerseTheme = {
        apply: applyTheme,
        current: loadTheme,
        toggle() {
            applyTheme(loadTheme() === "dark" ? "white" : "dark");
        }
    };

    document.addEventListener("DOMContentLoaded", () => {
        applyTheme(loadTheme());
        bindButtons();
    });

})();