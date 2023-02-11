<%*
	tp.file.move("export/to_export");
	await tp.user.remove_no_git_python();
	tp.file.move("articles/" + tp.file.title);
%>