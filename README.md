# Time Off Tracker

This is a Flask application that allows users to track and manage time off requests. The application is built using Python 3.11 and utilizes DynamoDB for data storage.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.11: [Download Python](https://www.python.org/downloads/)
- Flask: Install Flask using `pip install flask`
- Boto3: Install Boto3 using `pip install boto3`
- AWS credentials: Set up your AWS credentials to access DynamoDB. You can refer to the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) for more information.

## Setting up DynamoDB

1. Create an AWS account if you don't have one already.
2. Go to the AWS Management Console and open the DynamoDB service.
3. Create a new table named "time_off_requests" with the following attributes:
   - `id` (String): Primary key for the time off request.
   - `employee_name` (String): Name of the employee making the request.
   - `start_date` (String): Start date of the time off.
   - `end_date` (String): End date of the time off.
   - `status` (String): Status of the request (e.g., "pending", "approved", "rejected").
4. Note down the AWS region and the table name, as they will be needed for the application configuration.

## Configuration

1. Open the `config.py` file and update the following configuration variables:
   - `AWS_ACCESS_KEY`: Your AWS access key.
   - `AWS_SECRET_KEY`: Your AWS secret key.
   - `AWS_REGION`: The AWS region where your DynamoDB table is located.
   - `DYNAMODB_TABLE`: The name of the DynamoDB table for time off requests.
2. Save the `config.py` file.

## Running the Application

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the following command to start the Flask development server:

   ```bash
   python app.py
   ```

3. The application will be accessible at `http://localhost:5000` in your web browser.

## Usage

- Access the application in your web browser using the provided URL.
- Employees can submit time off requests by filling out the form with their details and clicking the "Submit" button.
- Managers can view and manage time off requests by navigating to the "Requests" page.
- Managers can approve or reject requests by clicking the corresponding buttons next to each request.
- All requests and their statuses are stored in DynamoDB and can be viewed on the "Requests" page.

## Folder Structure

- `app.py`: The main Flask application file.
- `config.py`: Configuration file for the application.
- `templates/`: Directory containing HTML templates for the application.
- `static/`: Directory containing static assets (CSS, JS, etc.) for the application.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).



---




[![Deploy to Cyclic](https://deploy.cyclic.app/button.svg)](https://deploy.cyclic.app/)

## Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

### Available Scripts

In the project directory, you can run:

#### `npm start`

Runs the app in the production mode.

#### `npm dev`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

#### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

#### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

#### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

### Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

#### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

#### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

#### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

#### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

#### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

#### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
