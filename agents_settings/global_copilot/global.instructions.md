Before using python command always check if there is local python environement in .venv or venv. If so, always use local environement.

Git push operations are available only for operator and are forbidden for agents. Agents cannot change anything on remote repository. Only local changes are allowed.

When looking for some code occurance in code files use ast-grep. It is installed globally. If you do not know that tool check (/home/tombed/agent_instructions/ast-grep_cli.md).
If with ast-grep your found result is 0, check always with grep or rg if there are really 0 occurances in case that pattern for ast-grep was wrongly created.

You are always allowed to run tests in pytest with python from local python envornement if it exists. If environement not exists, then ask me. 
