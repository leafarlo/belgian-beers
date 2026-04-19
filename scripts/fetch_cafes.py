import requests
import json
import os

# You must set this environment variable before running the script:
# export GOOGLE_MAPS_API_KEY="your_api_key_here"
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def fetch_brussels_cafes():
    if not API_KEY:
        print("Error: GOOGLE_MAPS_API_KEY environment variable is not set.")
        print("Usage: export GOOGLE_MAPS_API_KEY='your_api_key' && python3 fetch_cafes.py")
        return

    print("Fetching cafes in Brussels...")
    
    # 1. Text Search to find "beer cafes in Brussels"
    search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    search_params = {
        "query": "beer cafe in Brussels",
        "key": API_KEY,
        "type": "bar"
    }
    
    response = requests.get(search_url, params=search_params)
    results = response.json().get("results", [])
    
    new_cafes = []
    
    print(f"Found {len(results)} potential cafes. Fetching detailed opening hours...")
    
    for place in results:
        place_id = place.get("place_id")
        
        # 2. Place Details to get formatted opening hours
        details_url = "https://maps.googleapis.com/maps/api/place/details/json"
        details_params = {
            "place_id": place_id,
            "fields": "name,formatted_address,geometry,url,opening_hours",
            "key": API_KEY
        }
        
        details_res = requests.get(details_url, params=details_params).json().get("result", {})
        
        # Formatting opening hours (this can be complex from Google API, so we parse it to a simple string)
        hours_list = details_res.get("opening_hours", {}).get("weekday_text", [])
        formatted_hours = " | ".join(hours_list) if hours_list else "Hours not available"
        
        cafe = {
            "id": place_id,
            "name": details_res.get("name", place.get("name")),
            "address": details_res.get("formatted_address", place.get("formatted_address")),
            "lat": details_res.get("geometry", {}).get("location", {}).get("lat"),
            "lng": details_res.get("geometry", {}).get("location", {}).get("lng"),
            "sourceUrl": details_res.get("url", ""),
            "verifiedDate": "2026-04",
            "desc": "Imported from Google Maps.",
            "openingHours": formatted_hours,
            "tags": [], # MANUAL EFFORT REQUIRED: AI cannot accurately know the vibe tags
            "beers": [] # MANUAL EFFORT REQUIRED: You must manually check menus for specific beers
        }
        new_cafes.append(cafe)

    # Save to a temporary integration file so we don't overwrite our curated JSON.
    output_target = "../data/cafes_from_google.json"
    with open(output_target, "w", encoding="utf-8") as f:
        json.dump(new_cafes, f, indent=2, ensure_ascii=False)
        
    print(f"Done! Created {output_target}.")
    print("Action Required: Open the new JSON file, copy the cafes you want into data/cafes.json, and manually add their beer lists.")

if __name__ == "__main__":
    fetch_brussels_cafes()
