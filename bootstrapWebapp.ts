import * as fs from 'fs'
import axios from 'axios'
import { load } from 'js-yaml'
import path from 'path'
import recursiveReaddir from 'recursive-readdir'
import { Octokit } from '@octokit/rest'

export interface ProblemMetadata {
    url: string
    linkText: string
    time_complexity: string
    categories: string[]
    difficulty: {
        site: string
        perceived: string
    }
    resources: string[]
}

export interface Problem {
    number: number
    fileName: string
    filePath: string
    fileUrl: string
    metadata: ProblemMetadata
    createdAt: Date
    modifiedAt: Date
    language: Language
}

type Language =
    | 'JavaScript'
    | 'TypeScript'
    | 'Python'
    | 'Rust'
    | 'Go'
    | 'Unknown'

type FilePath = string

const DEFAULTPROBLEM_METADATA: ProblemMetadata = {
    url: '',
    linkText: '',
    time_complexity: '',
    categories: [],
    difficulty: {
        site: '',
        perceived: ''
    },
    resources: []
}

const REPO_PATH =
    'https://github.com/bluprince13/coding-interview-prep/blob/master'

function getLanguage(filePath: FilePath): Language {
    const extension = filePath.split('.').pop()?.toLowerCase()
    switch (extension) {
        case 'js':
            return 'JavaScript'
        case 'ts':
            return 'TypeScript'
        case 'py':
            return 'Python'
        case 'rs':
            return 'Rust'
        case 'go':
            return 'Go'
        default:
            return 'Unknown'
    }
}

function getLinkText(url: string): string {
    const urlObj = new URL(url)
    const domain = urlObj.hostname
    const segments = urlObj.pathname.split('/')
    const resource = segments[segments.length - 1]
    return `${domain} - ${resource}`
}

export const getProblems = async (): Promise<Problem[]> => {
    const problemFiles: FilePath[] = await recursiveReaddir('./src')
    let problems = problemFiles
        .filter((filePath) =>
            ['.rs', '.py', '.go', '.ts'].some((ext) => filePath.endsWith(ext))
        )
        .filter((filePath) => filePath.split('/').length > 2)
        .map((filePath) => {
            const contents = fs.readFileSync(filePath, 'utf8')
            const [, metadataStr] = contents.split('\n---')
            let metadata: ProblemMetadata | undefined
            if (metadataStr) {
                metadata = load(metadataStr.trim()) as ProblemMetadata
                metadata = {
                    ...metadata,
                    linkText: getLinkText(metadata.url)
                }
            }
            const { birthtime, mtime } = fs.statSync(filePath)
            const language = getLanguage(filePath)
            return {
                number: 0,
                fileName: path.basename(filePath),
                language,
                filePath,
                fileUrl: `${REPO_PATH}/${filePath}`,
                metadata: metadata || DEFAULTPROBLEM_METADATA,
                createdAt: birthtime,
                modifiedAt: mtime
            }
        })
    problems.sort((a, b) => a.createdAt.getTime() - b.createdAt.getTime())
    problems = problems.map((problem, index) => ({
        ...problem,
        number: index + 1
    }))
    return problems
}

const buildAssetsDirectory = 'webapp/src/buildAssets';
if (!fs.existsSync(buildAssetsDirectory)) {
  fs.mkdirSync(buildAssetsDirectory, { recursive: true });
  console.log(`Created directory ${buildAssetsDirectory}`);
} else {
  console.log(`Directory ${buildAssetsDirectory} already exists`);
interface FilesAndContents {
    [key: string]: string
}

const octokit = new Octokit({ auth: `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` });
let dirContentsConfig = {
    owner: "bluprince13",
    repo: "coding-interview-prep",
    path: "src"
  }

const getFilesAndContents = async () : Promise<FilesAndContents> => {
    const githubContents = await octokit.repos.getContent(dirContentsConfig);
    const files = githubContents.data
    const filesAndContents: FilesAndContents= {}
    await Promise.all(
        files.forEach(async (file: any) => {
            const contentsResponse = await axios.get(file.download_url)
            const contents = contentsResponse.data
            filesAndContents[file.name] = contents
        })
    )
    return filesAndContents
}

export const getProblems = async (filesAndContents: FilesAndContents): Promise<Problem[]> => {
    const problems = Object.entries(filesAndContents).map(
        ([file, contents]) => {
            const [, metadataStr] = contents.split('\n---')
            if (!metadataStr) return null
            const metadata = load(metadataStr.trim()) as ProblemMetadata
            return {
                filename: file.name,
                metadata,
                createdAt: new Date(file.created_at);
                modifiedAt: new Date(file.updated_at);
            }
        }
    )
    return problems.filter((problem) => !!problem)
}

getProblems().then((problems) => {
    const jsonData = JSON.stringify(problems)
    fs.writeFileSync(`${buildAssetsDirectory}/problems.json`, jsonData)
})

fs.copyFile(
    __filename,
    `${buildAssetsDirectory}/bootstrapWebapp.ts`,
    (error) => {
        if (error) {
            console.error(`Error copying file: ${error}`)
        }
    }
)
