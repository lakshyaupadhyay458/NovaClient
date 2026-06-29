package com.novaclient.mods;

public abstract class AbstractMod {

    private final String name;
    private final String description;
    private final ModCategory category;
    
    private boolean enabled;

    // Define structural categories common to performance PvP environments
    public enum ModCategory {
        HUD_DISPLAY,
        PERFORMANCE,
        COSMETIC,
        UTILITY
    }

    /**
     * Constructor: Enforces that every child mod must declare a name, description, and target category.
     */
    public AbstractMod(String name, String description, ModCategory category) {
        this.name = name;
        this.description = description;
        this.category = category;
        this.enabled = false; // All custom mods default to an off state until toggled
    }

    /**
     * Universal Gateway: Safely toggles the activation state of this mod feature.
     */
    public void toggle() {
        this.enabled = !this.enabled;
        System.out.println("[MOD ENGINE]: " + this.name + " state switched -> " + (this.enabled ? "ENABLED" : "DISABLED"));
        
        if (this.enabled) {
            onEnable();
        } else {
            onDisable();
        }
    }

    // Abstract lifecycle methods that individual child mods will implement to run their specific code
    public abstract void onEnable();
    public abstract void onDisable();
    public abstract void onTickUpdate();

    // Standard public getters to pass safe properties to our engine layouts
    public String getName() { return this.name; }
    public String getDescription() { return this.description; }
    public ModCategory getCategory() { return this.category; }
    public boolean isEnabled() { return this.enabled; }
    
    public void setEnabled(boolean state) {
        if (this.enabled != state) {
            toggle();
        }
    }
}