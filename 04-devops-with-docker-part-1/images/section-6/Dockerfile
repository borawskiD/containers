# We need Ruby 3.1.0
FROM ruby:3.1.0

# Expose the Rails server port
EXPOSE 3000

# Set the working directory
WORKDIR /usr/src/app

# Install the correct bundler version
RUN gem install bundler:2.3.3
RUN ls -la
# Copy Gemfile and Gemfile.lock for dependency installation
COPY Gemfile* ./
RUN ls -la
# Install Ruby gems
RUN bundle install

# Copy the remaining application source code
COPY . .

# Run database migrations
RUN rails db:migrate RAILS_ENV=production

# Precompile assets
RUN rake assets:precompile

# Start the Rails server
CMD ["rails", "s", "-e", "production"]
