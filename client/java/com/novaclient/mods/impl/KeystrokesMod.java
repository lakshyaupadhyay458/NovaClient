package com.novaclient.mods.impl;

import com.novaclient.mods.AbstractMod;

public class KeystrokesMod extends AbstractMod {

    // Movement state simulation variables
    private boolean wPressed = false;
    private boolean aPressed = false;
    private boolean sPressed = false;
    private boolean dPressed = false;

    public KeystrokesMod() {
        // Pass our mod details cleanly up to the parent AbstractMod constructor
        super("Keystrokes Display", "Shows a live HUD overlay of movement key selections.", ModCategory.HUD_DISPLAY);
    }

    @Override
    public void onEnable() {
        System.out.println("[KEYSTROKES MOD]: Hooking into global OS input listener frames...");
    }

    @Override
    public void onDisable() {
        System.out.println("[KEYSTROKES MOD]: Unhooking input streams. Clearing HUD state overlays...");
        clearPressedStates();
    }

    @Override
    public void onTickUpdate() {
        // If the mod is disabled, skip processing completely
        if (!isEnabled()) return;

        // Simulate a live gameplay movement state tracking cycle for testing verification
        simulateInputState();
    }

    /**
     * Clears our memory registers on disable to prevent frozen ghost keys on the screen.
     */
    private void clearPressedStates() {
        this.wPressed = false;
        this.aPressed = false;
        this.sPressed = false;
        this.dPressed = false;
    }

    /**
     * Simple simulation helper demonstrating real-time input capture tracking loops.
     */
    private void simulateInputState() {
        // Randomly simulate a key state change to prove the rendering metrics tracking works
        double rand = Math.random();
        if (rand > 0.8) {
            this.wPressed = !this.wPressed;
            if (wPressed) System.out.println("[KEYSTROKES OVERLAY DRAW]: [W] KEY PRESSED");
        }
    }

    // Public getters to allow our GUI layers to read key states for rendering colors
    public boolean isWPressed() { return this.wPressed; }
    public boolean isAPressed() { return this.aPressed; }
    public boolean isSPressed() { return this.sPressed; }
    public boolean isDPressed() { return this.dPressed; }
}