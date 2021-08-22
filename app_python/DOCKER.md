## Docker practices

* #### Create ephemeral containers

The container can be stopped and destroyed, then rebuilt and replaced with an absolute minimum set up and configuration.

* #### Exclude with .dockerignore

To exclude files not relevant to the build (without restructuring your source repository) use a `.dockerignore` file.

* #### Don’t install unnecessary packages

To reduce complexity, dependencies, file sizes, and build times, avoid installing extra or unnecessary packages just because they might be “nice to have.” For example, you don’t need to include a text editor in a database image.

* #### Decouple applications🔗

Each container should have only one concern. Decoupling applications into multiple containers makes it easier to scale horizontally and reuse containers. For instance, a web application stack might consist of three separate containers, each with its own unique image, to manage the web application, database, and an in-memory cache in a decoupled manner.

* #### Use multi-stage builds

Multi-stage builds allow you to drastically reduce the size of your final image, without struggling to reduce the number of intermediate layers and files. Because an image is built during the final stage of the build process, you can minimize image layers by leveraging build cache.

* #### Dockerfile instructions

Whenever possible, use current official images as the basis for your images. It is recommended to use the Alpine image as it is tightly controlled and small in size (currently under 6 MB), while still being a full Linux distribution.

Split long or complex `RUN` statements on multiple lines separated with backslashes to make your `Dockerfile` more readable, understandable, and maintainable.

