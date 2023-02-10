<%*
	tp.file.move("export/to_export");
	await tp.user.remove_python();
	tp.file.move("articles/" + tp.file.title);
%>