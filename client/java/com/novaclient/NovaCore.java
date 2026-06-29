package com.novaclient;

public class NovaCore {
    
    private static NovaCore instance;
    
    private final String clientName = "Nova Client";
    private final String clientVersion = "1.0.0-Alpha";
    private boolean isRunning = false;

    // Declare our Profile Manager reference variable
    private ProfileManager profileManager;

    private NovaCore() {
        // Instantiate our system controllers inside the private constructor
        this.profileManager = new ProfileManager();
    }

    private static class ProfileManager {
        private String activeProfile;

        public void setActiveProfile(String profile) {
            this.activeProfile = profile;
        }

        public String getActiveProfile() {
            return this.activeProfile;
        }
    }

    public static NovaCore getInstance() {
        if (instance == null) {
            instance = new NovaCore();
        }
        return instance;
    }

    public void initialize() {
        System.out.println("[" + clientName + "] Commencing core initialization sequence...");
        this.isRunning = true;
        
        System.out.println("[" + clientName + "] Running Version: " + clientVersion);
        
        // Trigger a profile verification pass to simulate launcher argument ingestion
        System.out.println("[" + clientName + "] Interrogating active launch arguments configuration...");
        profileManager.setActiveProfile("Nova Core (Latest)");
        
        System.out.println("[" + clientName + "] Core Engine state verified. Ready for execution.");
    }

    public void shutdown() {
        System.out.println("[" + clientName + "] Shutting down core engines safely.");
        this.isRunning = false;
    }

    // Expose a public getter so external mods can check profile settings
    public ProfileManager getProfileManager() { return this.profileManager; }
    public String getClientName() { return this.clientName; }
    public String getClientVersion() { return this.clientVersion; }
    public boolean isRunning() { return this.isRunning; }

    public static void main(String[] args) {
        NovaCore core = NovaCore.getInstance();
        core.initialize();
        core.shutdown();
    }
}