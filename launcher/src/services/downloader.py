import requests

class NovaDownloader:
    def __init__(self):
        """
        Constructor: Sets up the official modern Mojang version manifest endpoint URL.
        """
        # Updated to the official V2 Piston-Meta manifest endpoint
        self.manifest_url = "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"

    def fetch_available_versions(self):
        """
        Reaches out to Mojang's servers via HTTP to fetch the official list of live Minecraft versions.
        """
        print("NET SERVICE: Contacting Mojang meta servers to check versions...")
        
        try:
            response = requests.get(self.manifest_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                print("NET SERVICE: Version manifest fetched successfully!")
                return data
            else:
                print(f"NET SERVICE ERROR: Server replied with status code {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"NET SERVICE ERROR: Network connection failed. Details: {e}")
            return None