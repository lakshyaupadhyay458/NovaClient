package com.novaclient.profiles;

import java.util.HashMap;
import java.util.Map;

public class ProfileManager {

    // 1. Define our structural Client Profile Types using an Enum
    public enum ClientProfileType {
        PVP_OPTIMIZED,
        VANILLA_CLEAN,
        SURVIVAL_MODDED
    }

    private static final String DEFAULT_PROFILE_NAME = "Nova Core (Latest)";
    private static final ClientProfileType DEFAULT_PROFILE_TYPE = ClientProfileType.PVP_OPTIMIZED;

    // A memory map tracking all registered profiles by their display names
    private final Map<String, ClientProfileType> profileMap;
    private String activeProfileName;

    public ProfileManager() {
        this.profileMap = new HashMap<>();
        this.activeProfileName = DEFAULT_PROFILE_NAME;

        // Register our baseline structural configurations
        registerDefaultProfiles();
    }

    /**
     * Fills our system memory map with our core PvP and Vanilla operation modes.
     */
    private void registerDefaultProfiles() {
        profileMap.put("Nova Core (Latest)", ClientProfileType.PVP_OPTIMIZED);
        profileMap.put("Vanilla Experience", ClientProfileType.VANILLA_CLEAN);
        profileMap.put("Survival Toolkit", ClientProfileType.SURVIVAL_MODDED);
    }

    /**
     * Allows the engine runtime to dynamically switch operational client profiles.
     */
    public void setActiveProfile(String profileName) {
        if (profileMap.containsKey(profileName)) {
            this.activeProfileName = profileName;
            ClientProfileType type = profileMap.get(profileName);
            System.out.println("[PROFILE MANAGER]: Successfully loaded client runtime mode -> [" + type + "]");
        } else {
            System.out.println("[PROFILE MANAGER WARNING]: Unknown profile target '" + profileName + "'. Defaulting to PvP Core.");
            this.activeProfileName = "Nova Core (Latest)";
        }
    }

    // Public getters to safely share configuration data with the rest of our mods
    public String getActiveProfileName() { return this.activeProfileName; }
    public ClientProfileType getActiveProfileType() { return profileMap.get(this.activeProfileName); }
}