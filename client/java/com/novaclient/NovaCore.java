package com.novaclient;

public class NovaCore {
    
    // 1. Establish our Singleton instance variable reference
    private static NovaCore instance;
    
    // Core structural variables tracking client states
    private final String clientName = "Nova Client";
    private final String clientVersion = "1.0.0-Alpha";
    private boolean isRunning = false;

    /**
     * Constructor is explicitly marked 'private' to enforce the Singleton pattern,
     * preventing other files from accidentally creating duplicate core engines.
     */
    private NovaCore() {
        // Initialization code will hook here
    }

    /**
     * Global Gateway: Allows any mod or UI component to get a safe handle on our running core.
     */
    public static NovaCore getInstance() {
        if (instance == null) {
            instance = new NovaCore();
        }
        return instance;
    }

    /**
     * The primary initialization hook called right as the client engine initializes.
     */
    public void initialize() {
        System.out.println("[" + clientName + "] Commencing core initialization sequence...");
        this.isRunning = true;
        
        // 2. Log out our system states to verify the runtime environment setup
        System.out.println("[" + clientName + "] Running Version: " + clientVersion);
        System.out.println("[" + clientName + "] Core Engine state verified. Ready for mod profile ingestion pipeline.");
    }

    /**
     * Safe teardown hook triggered when the player exits the game application window.
     */
    public void shutdown() {
        System.out.println("[" + clientName + "] Shutting down core engines safely. Flushing cache states...");
        this.isRunning = false;
    }

    // Standard public getter methods to expose safe read-only access to variables
    public String getClientName() { return this.clientName; }
    public String getClientVersion() { return this.clientVersion; }
    public boolean isRunning() { return this.isRunning; }

    /**
     * Standard Java main method. Used for initial compilation testing.
     */
    public static void main(String[] args) {
        NovaCore core = NovaCore.getInstance();
        core.initialize();
        core.shutdown();
    }
}
