<script lang="ts">
	import problemsJson from '../buildAssets/problems.json';
	import type { Problem } from '../buildAssets/bootstrapWebapp';
	import _ from 'lodash';
	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell,
		TableSearch
	} from 'flowbite-svelte';
	const items: Problem[] = problemsJson;

	const filterByValue = (arr, str) => {
		return arr.filter((obj) => {
			console.log(JSON.stringify(obj).toLowerCase());
			return JSON.stringify(obj).toLowerCase().includes(str.toLowerCase());
		});
	};

	let searchTerm = '';
	$: filteredItems = filterByValue(items, searchTerm);
</script>

<h1>Coding problems</h1>
<Table hoverable={true} striped={true} shadow>
	<caption
		class="p-5 text-lg font-semibold text-left text-gray-900 bg-white dark:text-white dark:bg-gray-800"
	>
		Coding problems
		<p class="mt-1 text-sm font-normal text-gray-500 dark:text-gray-400">
			List of problems I have done.
		</p>
	</caption>
	<TableSearch placeholder="Search" hoverable={true} bind:inputValue={searchTerm}>
		<TableHead>
			<TableHeadCell>Number</TableHeadCell>
			<TableHeadCell>File</TableHeadCell>
			<TableHeadCell>Language</TableHeadCell>
			<TableHeadCell>Problem Source</TableHeadCell>
			<TableHeadCell>Difficulty</TableHeadCell>
			<TableHeadCell>Perceived difficulty</TableHeadCell>
			<TableHeadCell>Categories</TableHeadCell>
			<TableHeadCell>Created</TableHeadCell>
			<TableHeadCell>Modified</TableHeadCell>
		</TableHead>
		<TableBody tableBodyClass="divide-y">
			{#each filteredItems as item}
				<TableBodyRow class="table-row">
					<TableBodyCell>{item.number}</TableBodyCell>
					<TableBodyCell
						><a
							class="font-medium text-blue-600
				hover:underline dark:text-blue-500"
							href={item.fileUrl}>{item.fileName}</a
						></TableBodyCell
					>
					<TableBodyCell>{item.language}</TableBodyCell>
					<TableBodyCell
						><a
							class="font-medium text-blue-600
				hover:underline dark:text-blue-500"
							href={item.metadata.url}>{item.metadata.linkText}</a
						></TableBodyCell
					>
					<TableBodyCell>{item.metadata.difficulty.site}</TableBodyCell>
					<TableBodyCell>{item.metadata.difficulty.perceived}</TableBodyCell>
					<TableBodyCell>{item.metadata.categories.join(', ')}</TableBodyCell>
					<TableBodyCell>{new Date(item.createdAt).toLocaleDateString()}</TableBodyCell>
					<TableBodyCell>{new Date(item.modifiedAt).toLocaleDateString()}</TableBodyCell>
				</TableBodyRow>
			{/each}
		</TableBody>
	</TableSearch>
</Table>

<style>
</style>
