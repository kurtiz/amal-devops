import {Router} from "express";

/**
 * Main Router
 * @type {Router}
 */
const router = Router();


// home route just to show the site is working
router.get("/", (request, response) => {
    response.send(
        "<h1>Mini Server is Live</h1> <br>" +
        "<h2>Version: 1.0.0</h2><br>" +
        "<h3>Author: Aaron Will Djaba</h3>");
});

export default router;