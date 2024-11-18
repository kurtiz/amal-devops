import {server} from "./app.js";

/**
 * Starts the server
 */
server.listen(8080, () => {
    console.log(`Listening on http://localhost:8080`);
});