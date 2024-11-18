# Start from the official Alpine image
FROM alpine:latest

# Install required packages and dependencies in a single RUN step
RUN apk add --update nodejs=20.15.1-r0

RUN apk add --update npm

# Set working directory to /app
WORKDIR /app

# Copy application files into the container
COPY . .

# Install app dependencies (using npm)
RUN npm install

# Expose the app port
EXPOSE 8080

# Start the application
CMD ["npm", "run", "start"]
