<script lang="ts">
	import problemsJson from '../buildAssets/problems.json';
	import type { Problem } from '../buildAssets/bootstrapWebapp';
	const problems: Problem[] = problemsJson;
</script>

<div class="container mx-auto p-8 space-y-8">
	<h1>Coding problems</h1>
	<p>
		This is a UI for a collection of coding challenges that I've solved at <a
			href="https://github.com/bluprince13/coding-interview-prep">coding-interview-prep</a
		>.
	</p>

	<table>
		<thead>
			<tr>
				<th>Number</th>
				<th>File</th>
				<th>Language</th>
				<th>Problem Source</th>
				<th>Difficulty</th>
				<th>Perceived difficulty</th>
				<th>Categories</th>
			</tr>
		</thead>
		<tbody>
			{#each problems as problem}
				<tr>
					<td>{problem.number}</td>
					<td><a href={problem.fileUrl}>{problem.fileName}</a></td>
					<td>{problem.language}</td>
					<td><a href={problem.metadata.url}>{problem.metadata.linkText}</a></td>
					<td>{problem.metadata.difficulty.site}</td>
					<td>{problem.metadata.difficulty.perceived}</td>
					<td>{problem.metadata.categories.join(', ')}</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>

<style>
	table {
		border-collapse: collapse;
		width: 100%;
	}

	th,
	td {
		border: 1px solid black;
		padding: 8px;
	}
</style>
