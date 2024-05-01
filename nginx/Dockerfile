# Use an official Nginx image as the base image
FROM nginx:1.25

# Remove the default configuration file that comes with Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copy the custom Nginx configuration file to the container
COPY nginx.conf /etc/nginx/conf.d
