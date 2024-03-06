import csv

# Define the data
data = [
    {
        "question": "What is the difference between `==` and `===` operators in JavaScript?",
        "answer": "The `==` operator checks for equality after type coercion, while `===` checks for strict equality without type coercion."
    },
    {
        "question": "How can you prevent a JavaScript function from being called multiple times simultaneously?",
        "answer": "You can use a flag variable or a locking mechanism like a semaphore to ensure mutual exclusion while the function is executing."
    },
    {
        "question": "What is a closure in JavaScript?",
        "answer": "A closure is a combination of a function bundled together with references to its surrounding state, allowing it to retain access to variables from its lexical scope even after that scope has closed."
    },
    {
        "question": "How do you handle errors in asynchronous JavaScript code?",
        "answer": "You can use try-catch blocks or handle errors with promise `.catch()` methods in asynchronous JavaScript code."
    },
    {
        "question": "What are some ways to improve the performance of JavaScript code?",
        "answer": "Strategies include minimizing DOM manipulation, optimizing loops, caching variables, using event delegation, and employing asynchronous programming techniques."
    },
    {
        "question": "What are the differences between `let`, `const`, and `var` in JavaScript?",
        "answer": "`let` and `const` are block-scoped and `const` variables cannot be reassigned, while `var` is function-scoped and allows redeclaration and reassignment."
    },
    {
        "question": "How can you deep clone an object in JavaScript?",
        "answer": "You can use methods like `JSON.parse(JSON.stringify(object))`, third-party libraries like Lodash's `cloneDeep()`, or manually iterate through the object's properties and clone them."
    },
    {
        "question": "What is event bubbling and event capturing in JavaScript?",
        "answer": "Event bubbling is the propagation of events from the target element up to the document, while event capturing is the opposite, starting from the document down to the target element."
    },
    {
        "question": "How do you check if a variable is an array in JavaScript?",
        "answer": "You can use `Array.isArray(variable)` method to determine if a variable is an array."
    },
    {
        "question": "What is the purpose of the `use strict` directive in JavaScript?",
        "answer": "`use strict` is a directive that enables strict mode, which catches common coding errors and prevents the use of certain unsafe features in JavaScript."
    },
    {
        "question": "What is React?",
        "answer": "React is a JavaScript library for building user interfaces, developed by Facebook."
    },
    {
        "question": "What are the key features of React?",
        "answer": "Key features include virtual DOM for performance optimization, component-based architecture, JSX for declarative UI, and uni-directional data flow."
    },
    {
        "question": "What is JSX in React?",
        "answer": "JSX is a syntax extension for JavaScript that allows mixing HTML-like code within JavaScript code, used to describe the UI in React components."
    },
    {
        "question": "What are React components?",
        "answer": "React components are reusable and independent pieces of UI, encapsulating both the UI and the logic to manage it."
    },
    {
        "question": "What is state in React?",
        "answer": "State is an internal data storage mechanism used by React components to keep track of their own data."
    },
    {
        "question": "What is props in React?",
        "answer": "Props (short for properties) are a way of passing data from parent to child components in React."
    },
    {
        "question": "What is the difference between state and props in React?",
        "answer": "State is managed within a component and can be updated by that component, while props are passed from parent to child components and are immutable within the child."
    },
    {
        "question": "What is a React lifecycle?",
        "answer": "React lifecycle refers to the series of methods that are invoked in the process of creating, updating, and destroying a component."
    },
    {
        "question": "What are controlled components in React?",
        "answer": "Controlled components are React components whose form elements are fully controlled by React via state, enabling dynamic control over form inputs."
    },
    {
        "question": "What are hooks in React?",
        "answer": "Hooks are functions that enable functional components in React to use state and other React features without writing a class."
    },
    {
        "question": "What is Node.js?",
        "answer": "Node.js is a runtime environment for executing JavaScript code outside of a web browser, allowing server-side programming using JavaScript."
    },
    {
        "question": "What is npm?",
        "answer": "npm (Node Package Manager) is a package manager for Node.js, used to install, manage, and share JavaScript libraries and tools."
    },
    {
        "question": "How do you install Node.js?",
        "answer": "You can download and install Node.js from the official website or use a package manager like npm or yarn."
    },
    {
        "question": "How do you create a new npm package?",
        "answer": "You can initialize a new npm package by running `npm init` in your project directory and following the prompts, or use `npm init --yes` for a quick setup with default values."
    },
    {
        "question": "What is the purpose of package.json in Node.js?",
        "answer": "package.json is a metadata file used to describe a Node.js package, including its name, version, dependencies, scripts, and other metadata."
    },
    {
        "question": "How do you install dependencies using npm?",
        "answer": "You can install dependencies listed in the package.json file by running `npm install`, optionally with the `--save` or `--save-dev` flags to save them as dependencies or development dependencies, respectively."
    },
    {
        "question": "What is the difference between dependencies and devDependencies in package.json?",
        "answer": "Dependencies are required for the runtime functionality of the application, while devDependencies are only needed for development and testing purposes."
    },
    {
        "question": "How do you publish a package to the npm registry?",
        "answer": "You can publish a package to the npm registry by running `npm publish` in the root directory of your package after logging in with your npm account using `npm login`."
    },
    {
        "question": "What is npm CLI?",
        "answer": "npm CLI (Command Line Interface) is a set of command-line tools provided by npm for managing Node.js packages, including installing, publishing, updating, and managing dependencies."
    },
    {
        "question": "How do you update npm to the latest version?",
        "answer": "You can update npm to the latest version by running `npm install -g npm` to install the latest npm package globally."
    },
    {
        "question": "What is Node.js?",
        "answer": "Node.js is a runtime environment for executing JavaScript code outside of a web browser, allowing server-side programming using JavaScript."
    },
    {
        "question": "What is npm?",
        "answer": "npm (Node Package Manager) is a package manager for Node.js, used to install, manage, and share JavaScript libraries and tools."
    },
    {
        "question": "How do you install Node.js?",
        "answer": "You can download and install Node.js from the official website or use a package manager like npm or yarn."
    },
    {
        "question": "How do you create a new npm package?",
        "answer": "You can initialize a new npm package by running `npm init` in your project directory and following the prompts, or use `npm init --yes` for a quick setup with default values."
    },
    {
        "question": "What is the purpose of package.json in Node.js?",
        "answer": "package.json is a metadata file used to describe a Node.js package, including its name, version, dependencies, scripts, and other metadata."
    },
    {
        "question": "How do you install dependencies using npm?",
        "answer": "You can install dependencies listed in the package.json file by running `npm install`, optionally with the `--save` or `--save-dev` flags to save them as dependencies or development dependencies, respectively."
    },
    {
        "question": "What is the difference between dependencies and devDependencies in package.json?",
        "answer": "Dependencies are required for the runtime functionality of the application, while devDependencies are only needed for development and testing purposes."
    },
    {
        "question": "How do you publish a package to the npm registry?",
        "answer": "You can publish a package to the npm registry by running `npm publish` in the root directory of your package after logging in with your npm account using `npm login`."
    },
    {
        "question": "What is npm CLI?",
        "answer": "npm CLI (Command Line Interface) is a set of command-line tools provided by npm for managing Node.js packages, including installing, publishing, updating, and managing dependencies."
    },
    {
        "question": "How do you update npm to the latest version?",
        "answer": "You can update npm to the latest version by running `npm install -g npm` to install the latest npm package globally."
    },
    
    {
        "question": "What is Mongoose?",
        "answer": "Mongoose is an Object Data Modeling (ODM) library for MongoDB and Node.js, designed to work with MongoDB's document-oriented nature."
    },
    {
        "question": "How do you connect to MongoDB using Mongoose?",
        "answer": "You can connect to MongoDB using Mongoose by calling the `mongoose.connect()` method and passing the MongoDB connection URI."
    },
    {
        "question": "What are schemas in Mongoose?",
        "answer": "Schemas in Mongoose define the structure of documents within a collection, including the fields, data types, and validation rules."
    },
    {
        "question": "How do you define models in Mongoose?",
        "answer": "You can define models in Mongoose by creating a Mongoose schema and then compiling it into a model using the `mongoose.model()` method."
    },
    {
        "question": "What are virtuals in Mongoose?",
        "answer": "Virtuals in Mongoose are document properties that are not persisted to the database but are computed properties based on other fields."
    },
    {
        "question": "How do you perform CRUD operations with Mongoose?",
        "answer": "You can perform CRUD operations with Mongoose using methods like `save()` for creating, `find()` for reading, `updateOne()` for updating, and `deleteOne()` for deleting documents."
    },
    {
        "question": "What is middleware in Mongoose?",
        "answer": "Middleware in Mongoose are functions that are executed before or after certain operations, such as validation, saving, or removing documents."
    },
    {
        "question": "How do you handle relationships in Mongoose?",
        "answer": "You can handle relationships in Mongoose using references or embedding, where you either reference documents from other collections or embed them directly within documents."
    },
    {
        "question": "What is population in Mongoose?",
        "answer": "Population in Mongoose is the process of automatically replacing specified paths in a document with documents from other collections, based on specified criteria."
    },
    {
        "question": "How do you handle transactions in Mongoose?",
        "answer": "You can handle transactions in Mongoose using the `Session` object, which allows you to perform multiple operations within a transaction and either commit or abort the transaction."
    },
    {
        "question": "What is Next.js?",
        "answer": "Next.js is a React framework for building server-side rendered and statically generated web applications."
    },
    {
        "question": "What are the key features of Next.js?",
        "answer": "Key features include automatic code splitting, server-side rendering, static exporting, file-based routing, and API routes."
    },
    {
        "question": "How do you create a new Next.js app?",
        "answer": "You can create a new Next.js app by running `npx create-next-app` in your terminal and following the prompts, or use `yarn create next-app` if you prefer Yarn."
    },
    {
        "question": "What is server-side rendering (SSR) in Next.js?",
        "answer": "Server-side rendering in Next.js is the process of generating the initial HTML for a page on the server, allowing faster initial page loads and improved SEO."
    },
    {
        "question": "What is static site generation (SSG) in Next.js?",
        "answer": "Static site generation in Next.js is the process of pre-rendering pages at build time, resulting in HTML files that can be served statically, improving performance and scalability."
    },
    {
        "question": "How do you create dynamic routes in Next.js?",
        "answer": "You can create dynamic routes in Next.js by adding square brackets `[]` to a page filename in the `pages` directory, indicating that it's a dynamic route, and accessing the route parameters using `useRouter()` hook."
    },
    {
        "question": "What are API routes in Next.js?",
        "answer": "API routes in Next.js are special files inside the `pages/api` directory that allow you to build serverless API endpoints using Node.js and Express-like syntax."
    },
    {
        "question": "How do you deploy a Next.js app?",
        "answer": "You can deploy a Next.js app to various hosting platforms like Vercel, Netlify, or AWS by running `next build` to generate a production build, followed by deploying the generated `/.next` directory."
    },
    {
        "question": "What is the difference between `getStaticProps` and `getServerSideProps` in Next.js?",
        "answer": "`getStaticProps` is used for static site generation (SSG) and runs at build time, while `getServerSideProps` is used for server-side rendering (SSR) and runs on every request."
    },
    {
        "question": "How do you handle authentication in Next.js?",
        "answer": "You can handle authentication in Next.js using libraries like NextAuth.js, Auth0, or by implementing your custom authentication logic using session management or JWT tokens."
    },
    
    {
        "question": "What is Axios?",
        "answer": "Axios is a popular JavaScript library for making HTTP requests from the browser and Node.js, featuring easy-to-use API, promise-based asynchronous requests, and automatic JSON parsing."
    },
    {
        "question": "How do you install Axios?",
        "answer": "You can install Axios via npm or yarn by running `npm install axios` or `yarn add axios` in your project directory."
    },
    {
        "question": "How do you make a GET request using Axios?",
        "answer": "You can make a GET request using Axios by calling the `axios.get()` method and passing the URL as an argument."
    },
    {
        "question": "How do you make a POST request using Axios?",
        "answer": "You can make a POST request using Axios by calling the `axios.post()` method and passing the URL and data payload as arguments."
    },
    {
        "question": "What is the Axios interceptor?",
        "answer": "Axios interceptor is a middleware mechanism that allows you to intercept and modify HTTP requests or responses globally, applying custom logic such as adding headers or logging."
    },
    {
        "question": "How do you handle errors with Axios?",
        "answer": "You can handle errors with Axios by using the `.catch()` method on the promise returned by the request, and implementing error handling logic inside the catch block."
    },
    {
        "question": "How do you configure Axios to use base URL?",
        "answer": "You can configure Axios to use a base URL for all requests by creating an Axios instance with custom configuration using `axios.create()` and setting the `baseURL` option."
    },
    {
        "question": "What is Axios cancellation?",
        "answer": "Axios cancellation is the ability to cancel pending HTTP requests to prevent them from completing or executing callbacks, useful for scenarios like user navigation or component unmounting."
    },
    {
        "question": "How do you send HTTP headers with Axios requests?",
        "answer": "You can send HTTP headers with Axios requests by passing a headers object containing key-value pairs of headers as an optional argument to the request methods like `axios.get()` or `axios.post()`."
    },
    {
        "question": "How do you upload files using Axios?",
        "answer": "You can upload files using Axios by creating a FormData object, appending files to it, and then sending it in a POST request using `axios.post()` with the FormData object as the data payload."
    },
    {
        "question": "What is Tailwind CSS?",
        "answer": "Tailwind CSS is a utility-first CSS framework for building custom designs without writing CSS, featuring a low-level utility class approach and customizable design system."
    },
    {
        "question": "How do you install Tailwind CSS?",
        "answer": "You can install Tailwind CSS via npm or yarn by running `npm install tailwindcss` or `yarn add tailwindcss` in your project directory, followed by configuring it for your build process."
    },
    {
        "question": "What is a utility class in Tailwind CSS?",
        "answer": "A utility class in Tailwind CSS is a CSS class that applies a single CSS property or a set of related CSS properties using a specific naming convention, allowing rapid prototyping and customization."
    },
    {
        "question": "How do you configure Tailwind CSS?",
        "answer": "You can configure Tailwind CSS by creating a `tailwind.config.js` file in your project directory and customizing various configuration options such as colors, typography, spacing, and more."
    },
    {
        "question": "What is JIT mode in Tailwind CSS?",
        "answer": "JIT (Just-In-Time) mode in Tailwind CSS is a build mode that dynamically generates CSS on-demand as you write HTML, allowing for faster development and smaller bundle sizes."
    },
    {
        "question": "How do you use responsive design with Tailwind CSS?",
        "answer": "You can use responsive design with Tailwind CSS by adding responsive utility classes like `sm:`, `md:`, `lg:`, and `xl:` to apply styles at specific breakpoints, or by using the `@media` directive in custom CSS."
    },
    {
        "question": "What is the purpose of PurgeCSS in Tailwind CSS?",
        "answer": "PurgeCSS is a tool used to remove unused CSS styles from your production bundle, reducing the file size and improving performance by only including the styles that are actually used."
    },
    {
        "question": "How do you extend Tailwind CSS with custom styles?",
        "answer": "You can extend Tailwind CSS with custom styles by using the `@layer` directive to insert custom CSS rules at specific layers in the generated stylesheet, or by using plugins to add new utility classes or components."
    },
    {
        "question": "What are the advantages of Tailwind CSS?",
        "answer": "Advantages include rapid prototyping, consistent design system, reduced need for writing custom CSS, improved developer experience, and easier collaboration between designers and developers."
    },
    {
        "question": "How do you integrate Tailwind CSS with frameworks like React or Vue.js?",
        "answer": "You can integrate Tailwind CSS with frameworks like React or Vue.js by installing the necessary dependencies, configuring Tailwind CSS for your build process, and using utility classes directly in your components."
    },
    {
        "question": "What is Vite?",
        "answer": "Vite is a next-generation frontend build tool for modern web development, designed to provide faster development server startup, instant hot module replacement (HMR), and optimized production builds."
    },
    {
        "question": "How do you create a new project with Vite?",
        "answer": "You can create a new project with Vite by running `npm init @vitejs/app` or `yarn create @vitejs/app` and selecting a template like Vue, React, or Vanilla JavaScript, followed by configuring the project settings."
    },
    {
        "question": "What is the purpose of Vite's dev server?",
        "answer": "Vite's dev server provides a fast development environment with instant server startup, optimized build times, and hot module replacement (HMR) for fast feedback during development."
    },
    {
        "question": "How does Vite achieve faster development server startup?",
        "answer": "Vite achieves faster development server startup by leveraging ES module imports, serving code directly from source files without bundling, and using optimized development server architecture."
    },
    {
        "question": "What is HMR (Hot Module Replacement) in Vite?",
        "answer": "HMR (Hot Module Replacement) in Vite is a feature that updates modules in the browser without a full page reload, providing a faster development experience by preserving application state."
    },
    {
        "question": "How do you configure Vite for production builds?",
        "answer": "You can configure Vite for production builds by customizing the `vite.config.js` file, optimizing build settings, and running `vite build` to generate optimized production assets."
    },
    {
        "question": "What is Vite's plugin system?",
        "answer": "Vite's plugin system allows developers to extend Vite's functionality by writing custom plugins, which can modify the build pipeline, provide custom features, or integrate with third-party tools."
    },
    {
        "question": "How do you use Vite with frameworks like Vue.js or React?",
        "answer": "You can use Vite with frameworks like Vue.js or React by installing the necessary dependencies, configuring Vite to support the framework's development environment, and creating project files using the framework's conventions."
    },
    {
        "question": "What are the advantages of using Vite?",
        "answer": "Advantages include faster development server startup, instant hot module replacement (HMR), optimized production builds, ES module support, and seamless integration with modern frontend frameworks."
    },
    {
        "question": "How does Vite compare to other build tools like webpack or Rollup?",
        "answer": "Vite provides faster development server startup and hot module replacement (HMR) compared to webpack and Rollup, thanks to its use of ES module imports and optimized development server architecture."
    }
]

# Define the file path
file_path = "questions_answers.csv"

# Write the data to a CSV file
with open(file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["question", "answer"])  # Write the header
    for item in data:
        writer.writerow([item["question"], item["answer"]])  # Write the data
