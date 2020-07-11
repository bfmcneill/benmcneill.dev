Title: Git Submodules
Date: 2020-07-10 10:20
Modified: 2020-07-10 19:30
Category: Dev Resources
Tags: git, advanced-git
Slug: git-sub-modules
Author: Ben McNeill
cover_image: https://images.unsplash.com/photo-1465146344425-f00d5f5c8f07?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1510&q=80
cover_image_by: Henry Be
cover_image_link: https://unsplash.com/photos/IicyiaPYGGI

<!-- {% img {static|/extra/cactus.jpg} 200 200 "Cactus" "Alt text" %} -->

When it comes to understanding git submodules things can get tricky real quick.  One of the best resources I have found so far on how to work with them is [this](https://www.youtube.com/watch?v=UQvXst5I41I) video.

You might be wondering what kind of use case does a git submodule apply to.  This blog for example has a theme maintained by a 3rd party repo.  I don't have any immediate intention to PR any code to that repo and would rather have a way to pull the code into this blog project if need be.  What I can do is place that 3rd party code in the themes directory and now I can work with it even though it has it's own git log.  All my project cares about what commit it needs to reference in teh submodule.  If I want to change the commit my blog points to in the submodule I go into that directory and change the branch.

the main commands from this video are:

```bash
git submodule add <url> path_to_submodule
```

- `git submodule add` the command to add a sub module to your project
- `<url>` the git repo url
- `path_to_submodule` where you want it to exist in your super project

{% youtube UQvXst5I41I [40] [30] %}



