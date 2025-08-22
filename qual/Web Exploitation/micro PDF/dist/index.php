<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PDF Header Adder</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">

    <div class="w-full max-w-lg mx-auto bg-white p-8 rounded-xl shadow-lg">
        <h1 class="text-2xl font-bold text-gray-800 text-center mb-2">PDF Header Adder</h1>
        <p class="text-center text-gray-500 mb-6">Upload a PDF and provide a URL to add a custom header to each page.</p>

        <form action="process.php" method="post" enctype="multipart/form-data" class="space-y-6">
            <div>
                <label for="pdf_file" class="block text-sm font-medium text-gray-700 mb-1">1. Choose PDF File</label>
                <input type="file" name="pdf_file" id="pdf_file" required accept=".pdf"
                       class="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 transition-colors duration-200 cursor-pointer border rounded-lg">
            </div>

            <div>
                <label for="header_url" class="block text-sm font-medium text-gray-700 mb-1">2. Header Content URL</label>
                <input type="url" name="header_url" id="header_url" required
                       placeholder="https://api.example.com/header_text"
                       class="mt-1 block w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm">
                <p class="text-xs text-gray-500 mt-2">The text content from this URL will be used as the header.</p>
            </div>

            <div>
                <button type="submit"
                        class="w-full flex justify-center py-3 px-4 border border-transparent rounded-lg shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-transform transform hover:scale-105">
                    Add Header & Download PDF
                </button>
            </div>
        </form>

        <?php if (isset($_GET['error'])): ?>
            <div class="mt-6 p-4 bg-red-100 border border-red-400 text-red-700 rounded-lg">
                <strong>Error:</strong> <?php echo htmlspecialchars($_GET['error']); ?>
            </div>
        <?php endif; ?>
    </div>

</body>
</html>
