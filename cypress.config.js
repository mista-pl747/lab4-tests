const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    projectId: "23vnc7",
    baseUrl: "http://127.0.0.1:8000",    

    specPattern: "cypress/e2e/**/*.cy.js",

    supportFile: false,
    video: false,
    screenshotOnRunFailure: false,
    
    setupNodeEvents(on, config) {
    },
  },
});