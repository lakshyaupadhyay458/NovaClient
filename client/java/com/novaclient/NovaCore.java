package com.novaclient;

import com.novaclient.profiles.ProfileManager;
// Import our new Client Engine heartbeat tool
import com.novaclient.engine.ClientEngine;

public class NovaCore {
    
    private static NovaCore instance;
    
    private final String clientName = "Nova Client";
    private final String clientVersion = "1.0.0-Alpha";
    private boolean isRunning = false;

    private ProfileManager profileManager;
    // Declare our Client Engine reference variable
    private ClientEngine clientEngine;

    private NovaCore() {
        this.profileManager = new ProfileManager();
        // Instantiate the background engine instance
        this.clientEngine = new ClientEngine();
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
        
        System.out.println("[" + clientName + "] Interrogating active launch arguments configuration...");
        profileManager.setActiveProfile("Nova Core (Latest)");
        
        // Start our core performance heartbeat loop!
        this.clientEngine.startEngine();
        
        System.out.println("[" + clientName + "] Core Engine state verified. Initialization complete.");
    }

    public void shutdown() {
        // Make sure to stop our running engine thread cleanly on close
        this.clientEngine.stopEngine();
        System.out.println("[" + clientName + "] Shutting down core engines safely.");
        this.isRunning = false;
    }

    public ClientEngine getClientEngine() { return this.clientEngine; }
    public ProfileManager getProfileManager() { return this.profileManager; }
    public String getClientName() { return this.clientName; }
    public String getClientVersion() { return this.clientVersion; }
    public boolean isRunning() { return this.isRunning; }

public static void main(String[] args) {
        NovaCore core = NovaCore.getInstance();
        core.initialize();
        
        // Keep the master main execution thread alive as long as our custom engine loop is actively tracking
        while (core.isRunning()) {
            try {
                Thread.sleep(100); // Check engine health status cycles every 100 milliseconds
            } catch (InterruptedException e) {
                System.out.println("[NOVA CORE EXCEPTION]: Master application loop thread interrupted.");
                Thread.currentThread().interrupt();
                break;
            }
        }
        
        core.shutdown();
    }