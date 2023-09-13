<%*
	let path = tp.file.path(relative=true).slice(0,-3);
	tp.file.move("export/to_export");
	await tp.user.remove_python();
	tp.file.move(path);
%>