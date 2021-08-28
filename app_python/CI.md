## CI practices

* #### Maintain a Code Repository

There should be a revision control system for the project’s source code. All artifacts required to build the project should be placed in the repository. The system should be buildable from a fresh checkout and not require additional dependencies. 

* #### Make it Easy to Get Latest Deliverables

Builds should be readily available to stakeholders and testers, to reduce the amount of rework necessary when rebuilding a feature that doesn’t meet requirements. Early testing should be done to reduce the chances that defects survive to deployment; early discovery of errors can reduce the amount of work necessary to resolve them.

* #### Everyone Can See the Latest Build

It should be easy to find out whether the build breaks and, if so, who made the relevant change.

## CI practices for Git Actions

* #### Keep your Actions minimal

The longer an action takes to set up and run, the more time you spend waiting. if your Action runs in a container, make sure to use a light Docker image, such as alpine or alpine-node, and install as little as possible to keep down the time your Action is running, from initial boot up to having finishing its run.

* ####  Don’t install dependencies unnecessarily

Avoid installing dependencies where you can. Make sure to take advantage of GitHub’s caching mechanism.

* #### Never hardcode secrets

Instead of manually hardcoding secrets into your workflow (whether it’s private or public), set them manually in the repository settings and access them using environment variables or step inputs.

* #### Limit environment variables

Prevent polluting the global environment context as much as possible by always declaring environment variables with the narrowest possible scope.

* #### Authors

Store authors in Action metadata to promote code ownership to be in charge of maintaining the action and answer questions about it.

## CI practices for Jenkins

* #### Keep Jenkins Secure At All Times

Jenkins does not perform any security checks within the default configuration. This implies that any user accessing the website can execute any random code on the Jenkins master. It is recommended to secure Jenkins and configure the ‘Configure Global Security’ option. 

* #### Always Backup The “JENKINS_HOME” Directory

Jenkins home directory contains lots of data, including job configurations, build logs, plugin configs, etc. that we cannot afford to lose. This can be accomplished through plugins offered by Jenkins or configuring a job to take backup. 

* #### Setup A Different Job/Project For Each Maintenance Or Development Branch Created

Setting up different jobs/projects for each branch helps you support parallel development efforts and maximize the advantage of sleuthing issues, thereby reducing risk and allowing developers to be more productive.

* #### Build A Scalable Jenkins Pipeline

Shared Libraries offer a version-controlled Pipeline code that can be stored and accessed from your source control management compared to a common programming library. 

* #### Manage Declarative Syntax/Declarative Pipelines

Declarative Pipelines configuration tells a system what to do, shifting the complexity of ‘how to do’ to the system.

* #### Monitor Your CI/CD Pipeline

Having a broken CI/CD pipeline can potentially stall your development team. Also, external dependencies like cloud services, network, testing services might affect your CI/CD pipeline, and you need to know when these occasional failures become significant enough to warrant action.


