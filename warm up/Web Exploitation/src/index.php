<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ping Service</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            --dark-bg: #1a1d29;
            --card-bg: #2d3748;
            --text-light: #e2e8f0;
            --border-color: #4a5568;
        }

        body {
            background: var(--dark-bg);
            color: var(--text-light);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            min-height: 100vh;
        }

        .hero-section {
            background: var(--primary-gradient);
            padding: 3rem 0;
            position: relative;
            overflow: hidden;
        }

        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
            opacity: 0.3;
        }

        .hero-content {
            position: relative;
            z-index: 2;
        }

        .main-container {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 1rem;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
            margin-top: -2rem;
            position: relative;
            z-index: 3;
        }

        .description-box {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 0.75rem;
            padding: 1.5rem;
            margin-bottom: 2rem;
        }

        .form-control {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: var(--text-light);
            border-radius: 0.5rem;
            padding: 0.75rem 1rem;
            font-size: 1rem;
        }

        .form-control:focus {
            background: rgba(255, 255, 255, 0.15);
            border-color: #667eea;
            box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
            color: var(--text-light);
        }

        .form-control::placeholder {
            color: rgba(226, 232, 240, 0.6);
        }

        .btn-primary {
            background: var(--secondary-gradient);
            border: none;
            border-radius: 0.5rem;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 16px rgba(245, 87, 108, 0.3);
            background: var(--secondary-gradient);
        }

        .output-section {
            background: #0f172a;
            border: 1px solid #334155;
            border-radius: 0.75rem;
            padding: 1.5rem;
            margin-top: 1.5rem;
            font-family: 'Courier New', monospace;
            min-height: 150px;
            white-space: pre-wrap;
        }

        .input-group {
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            border-radius: 0.5rem;
            overflow: hidden;
        }

        .network-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            opacity: 0.1;
            background-image: 
                radial-gradient(circle at 20% 80%, rgba(102, 126, 234, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(118, 75, 162, 0.3) 0%, transparent 50%);
        }

        .pulse-animation {
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.02); }
            100% { transform: scale(1); }
        }

        .status-indicator {
            display: inline-block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            margin-right: 8px;
            animation: blink 1s infinite;
        }

        .status-online {
            background-color: #10b981;
        }

        .status-offline {
            background-color: #ef4444;
        }

        @keyframes blink {
            0%, 50% { opacity: 1; }
            51%, 100% { opacity: 0.3; }
        }
    </style>
</head>
<body>
    <div class="network-bg"></div>
    
    <!-- Hero Section -->
    <section class="hero-section">
        <div class="container hero-content text-center">
            <h1 class="display-5 fw-bold mb-3">
                <i class="fas fa-satellite-dish me-3"></i>
                Send your IP
            </h1>
            <p class="lead mb-0">Network Connectivity Testing Service</p>
        </div>
    </section>

    <!-- Main Content -->
    <div class="container">
        <div class="main-container p-5 mb-4 rounded-3">
            <div class="container-fluid py-3">
                <!-- Description -->
                <div class="description-box">
                    <div class="d-flex align-items-center mb-3">
                        <i class="fas fa-info-circle me-2 text-primary"></i>
                        <strong>Service Description</strong>
                    </div>
                    <p class="mb-0">
                        The "check IP with ping" service allows users to input an IP address and performs a ping operation on that address. 
                        It sends several network packets to the specified IP and waits for a response. The service then displays the results of 
                        the ping operation, including information on the number of packets transmitted and received. Based on the results, it provides feedback, 
                        such as whether the IP is responsive or not. This service is commonly used to test the reachability and responsiveness of a given IP address, making it useful for network troubleshooting and diagnostics.
                    </p>
                </div>

                <!-- Form -->
                <form method="POST" action="index.php">
                    <div class="input-group mb-3">
                        <span class="input-group-text bg-dark border-secondary text-light">
                            <i class="fas fa-globe"></i>
                        </span>
                        <input type="text" name="ip" class="form-control col-4" placeholder="8.8.8.8">
                        <div class="input-group-append">
                            <input type="submit" class="btn btn-primary pulse-animation" value="Submit">
                        </div>
                    </div>
                </form>

                <!-- Output Section -->
                <div class="output-section">
                    <div class="d-flex align-items-center mb-3">
                        <i class="fas fa-terminal me-2"></i>
                        <strong>Ping Results:</strong>
                    </div>
                    <?php
                    error_reporting(0);
                    $ip = (string)($_POST["ip"]);
                    $response = shell_exec("ping -c 3 " . $ip);
                    echo ("\n".$response);
                    $receive = preg_match("/3 packets transmitted, (.*) received/s", $response, $out);
                    if ($out[1] == "3") {
                            echo "Ping Komedi";
                    } elseif ($out[1] == "0") {
                            echo "Send another IP please";
                    }
                    ?>
                </div>
                
                <!-- Status Indicators -->
                <?php if (isset($_POST["ip"])): ?>
                <div class="mt-3">
                    <?php if ($out[1] == "3"): ?>
                        <div class="text-success">
                            <span class="status-indicator status-online"></span>
                            <strong>Status: Online & Responsive</strong>
                        </div>
                    <?php elseif ($out[1] == "0"): ?>
                        <div class="text-danger">
                            <span class="status-indicator status-offline"></span>
                            <strong>Status: Offline or Unreachable</strong>
                        </div>
                    <?php endif; ?>
                </div>
                <?php endif; ?>
            </div>
        </div>
    </div>
    
    <!-- Temukan flag di / -->
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js"></script>
    <script>
        // Add interactive background effect
        document.addEventListener('mousemove', function(e) {
            const bg = document.querySelector('.network-bg');
            const x = (e.clientX / window.innerWidth) * 100;
            const y = (e.clientY / window.innerHeight) * 100;
            bg.style.background = `
                radial-gradient(circle at ${x}% ${y}%, rgba(102, 126, 234, 0.3) 0%, transparent 50%),
                radial-gradient(circle at ${80-x/2}% ${20+y/2}%, rgba(118, 75, 162, 0.3) 0%, transparent 50%)
            `;
        });
    </script>
</body>
</html>