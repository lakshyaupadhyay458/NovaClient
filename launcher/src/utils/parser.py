class NovaDataParser:
    @staticmethod
    def extract_release_versions(raw_manifest: dict) -> list:
        """
        Takes Mojang's massive master version data dictionary and extracts
        only the official clean consumer releases, filtering out snapshots and betas.
        """
        print("UTILS PARSER: Filtering version manifest dataset...")
        
        # Create an empty list to store our cleaned up version string names
        clean_releases = []
        
        # Ensure the data passed in isn't empty and contains the core 'versions' list block
        if not raw_manifest or "versions" not in raw_manifest:
            print("UTILS PARSER ERROR: Invalid manifest structure provided.")
            return clean_releases

        # Loop through every individual version item inside the manifest list array
        for version_entry in raw_manifest["versions"]:
            # Check the 'type' value. We only care about major production updates ('release')
            if version_entry.get("type") == "release":
                version_id = version_entry.get("id") # Extract the numeric name (e.g., "1.21")
                if version_id:
                    clean_releases.append(version_id)
                    
        print(f"UTILS PARSER: Successfully extracted {len(clean_releases)} production release targets.")
        return clean_releases