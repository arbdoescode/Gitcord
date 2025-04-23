import asyncio
import util.githubcommit as githubcommit

async def main():
    repo_owner = "arbdoescode"
    repo_name = "Gitcord"

    raw_commits =  githubcommit.fetch_commits(repo_owner, repo_name)
    formatted_commits = githubcommit.format_commits(raw_commits)

    print(formatted_commits)


if __name__ == "__main__":
    asyncio.run(main())