For Developer

# GIT branching model - Operational policy 
[Document](https://nvie.com/posts/a-successful-git-branching-model/)
## Rules
Rules for creating branches
In the case of new development, create it on a screen basis
Naming convention: feature/[screen ID/screen name]
Commit: Make it functional unit
ex:
Branch name: feature/customer_registration_screen
Commit: [feat] customer registration function development
Commit: [feat] Develop customer registration part of external system

When releasing, create a branch for release (created and merged each time at the time of release)
Naming convention: release_yyyymmdd_[environment]
Commit: Make it functional unit
release_yyyymmdd_[environment]
ex:
release_yyyymmdd_production
release_yyyymmdd_staging
##Operational policy 
- Commit message prefix
- Prefix 
| feat          | (formatting, missing semi colons, etc; no production code change)       | 
| fix           | (bug fix for the user, not a fix to a build script)                     |
| docs          | (changes to the documentation)                                          |
| style         | (formatting, missing semi colons, etc; no production code change)       |
| refactor      | (refactoring production code, eg. renaming a variable)                  |
| test          | (adding missing tests, refactoring tests; no production code change)    |
| chore         | chore (updating grunt tasks etc; no production code change)             |
    
## Git Branch Naming Conventions
- The main branches :
    - master
    - develop 
    - feature
    - release
- Branch naming convention:
    - anything except master, develop, release-*, or hotfix-*
    - hotfix-*
    - release-*