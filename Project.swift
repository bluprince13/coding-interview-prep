import ProjectDescription

let schemes: [Scheme] = [
  .scheme(
    name: "CodingInterviewPrep",
    shared: true,
    buildAction: .buildAction(targets: ["src"]),
    runAction: .runAction(
      configuration: .debug,
      arguments: nil
    )
  )
]

let project = Project(
  name: "CodingInterviewPrep",
  targets: [
    .target(
      name: "NetWorthTrackerTests",
      destinations: .macOS,
      product: .unitTests,
      bundleId: "io.tuist.CodingInterviewPrep",
      infoPlist: .default,
      sources: ["src/**"],
      resources: []
    )
  ],
  schemes: schemes
)
