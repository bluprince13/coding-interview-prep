import ProjectDescription

let project = Project(
    name: "CodingInterviewPrep",
    targets: [
        // Creating an empty app target even though we don't have any source files
        // Otherwise, tuist test will fail with `We couldn't find a build configuration of variant 'debug' for caching
        .target(
            name: "CodingInterviewPrep",
            destinations: .macOS,
            product: .app,
            bundleId: "io.tuist.CodingInterviewPrep",
            sources: [""]
        ),
        .target(
            name: "CodingInterviewPrepTests",
            destinations: .macOS,
            product: .unitTests,
            bundleId: "io.tuist.CodingInterviewPrepTests",
            sources: ["src/**"]
        ),
    ]
)
