import * as fs from 'fs'
import { load } from 'js-yaml'
import recursiveReaddir from 'recursive-readdir'

export interface ProblemMetadata {
    url: string
    time_complexity: string
    categories: string[]
    difficulty: {
        site: string
        perceived: string
    }
    resources: string[]
}

export interface Problem {
    filename: string
    metadata: ProblemMetadata
    createdAt: Date
    modifiedAt: Date
}

export const getProblems = async (): Promise<Problem[]> => {
    const problemFiles = await recursiveReaddir('./src')
    console.log(problemFiles)
    const problems = problemFiles.map((filename) => {
        const contents = fs.readFileSync(filename, 'utf8')
        const [, metadataStr] = contents.split('\n---')
        if (!metadataStr) return null
        const metadata = load(metadataStr.trim()) as ProblemMetadata
        const { birthtime, mtime } = fs.statSync(filename)
        return {
            filename,
            metadata,
            createdAt: birthtime,
            modifiedAt: mtime
        }
    })
    return problems.filter((problem) => !!problem)
}

getProblems().then((problems) => {
    const jsonData = JSON.stringify(problems)
    fs.writeFileSync('webapp/src/data/problems.json', jsonData)
})
