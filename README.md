# Move-In Floor Planner

Plan a move on a tablet or computer:

- **Floor plan:** draw the apartment to scale (or trace your listing's floor plan image), then drag real-size furniture in to check what fits.
- **Room look:** add product photos from IKEA, Walmart or any shop, place them in a room picture, and save the result as an image. Plain white backgrounds are removed automatically, and pieces with a real height or width are sized to the room.

Live site: https://ellielauk.github.io/move-in-floor-planner/

Plans and images are saved in the visitor's own browser (localStorage and IndexedDB). Nothing is uploaded.

- **Notes:** with ✎ Draw, write and sketch on the plan with Apple Pencil (pressure-sensitive, palm ignored, fingers still pan and zoom), or add typed notes that work with Scribble.

## On iPad

Open the site in Safari, tap Share → **Add to Home Screen**, and use it from the Home Screen icon. Safari can clear saved data for websites you haven't opened in a while; Home Screen apps keep theirs.

## Offline

`sw.js` (a service worker) caches the app after the first visit, so it opens and works with no connection. Pages load from the network first when online, so updates still arrive. Fonts fall back to system fonts if they were never cached.

## Editing

- `src/app.html` is the source. It's also published as a Claude artifact, so it has no `<html>`/`<head>` wrapper.
- Run `python3 build.py` to regenerate `index.html`, the page GitHub Pages serves.

## Deploy

GitHub Pages serves `main` from the repo root. Push to `main` and it redeploys within a minute or two.
