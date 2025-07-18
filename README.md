# CognitiveLedger: Federated Learning on-Chain via Homomorphic Encryption

Decentralized AI model governance and incentivized data provenance using federated learning and blockchain technology.

CognitiveLedger addresses the growing need for secure, transparent, and accountable artificial intelligence development. This project leverages the power of federated learning, homomorphic encryption, and blockchain technology to enable decentralized AI model training while ensuring data privacy and provenance. Traditional centralized AI model training often requires sharing sensitive data with a central authority, raising concerns about privacy breaches and data misuse. CognitiveLedger overcomes this limitation by allowing multiple participants to collaboratively train an AI model without revealing their raw data. This is achieved through federated learning, where local models are trained on individual devices and only model updates are shared with a central aggregator.

Further enhancing security and privacy, CognitiveLedger employs homomorphic encryption. This advanced cryptographic technique allows computations to be performed on encrypted data without decryption. This means that the central aggregator can perform operations on the encrypted model updates from different participants to create a global model update, all while maintaining the confidentiality of the underlying data. The resulting global model update is then broadcast to all participants, improving the accuracy of their local models.

The project also integrates blockchain technology to provide a transparent and immutable record of the model training process. Each model update, along with its associated metadata (e.g., participant identity, training parameters, contribution quality), is recorded on the blockchain. This creates a verifiable audit trail, enabling decentralized AI model governance and ensuring the integrity of the training process. Furthermore, CognitiveLedger incorporates incentivization mechanisms, allowing participants to be rewarded for contributing high-quality data and computational resources. This encourages widespread participation and ensures the long-term sustainability of the decentralized AI ecosystem.

**Key Features**

*   **Federated Learning Implementation:** Implements a robust federated learning framework using a parameter averaging approach. Local models are trained using TensorFlow/Keras and aggregated using weighted averaging based on the number of samples used for training. The framework is designed to support different model architectures and training algorithms.
*   **Homomorphic Encryption (HE) Integration:** Integrates the Paillier cryptosystem for homomorphic encryption of model updates. This ensures that the central aggregator can perform computations on the encrypted data without having access to the underlying raw data, guaranteeing privacy. We use a custom implementation leveraging optimized mathematical libraries for efficient HE operations.
*   **Blockchain-Based Provenance Tracking:** Utilizes a private Ethereum blockchain to record all model updates, participant contributions, and training parameters. Smart contracts are used to manage access control, verify model updates, and distribute rewards to participants based on their contributions.
*   **Decentralized Model Governance:** Implements a voting mechanism through smart contracts that allows participants to vote on model parameters, training strategies, and access control policies. This ensures that the model is developed and governed in a decentralized and transparent manner.
*   **Incentivized Data Contribution:** Implements a reward system based on tokenomics. Participants are rewarded with tokens for contributing high-quality data and computational resources. The token distribution is managed by smart contracts and dynamically adjusted based on the quality and quantity of contributions.
*   **Modular Design:** The codebase is designed with a modular architecture, allowing for easy integration of new features, such as different homomorphic encryption schemes, consensus mechanisms, and incentive structures.
*   **Secure Aggregation:** Implements secure aggregation techniques to protect against malicious actors attempting to inject biased model updates. This includes techniques such as differential privacy and secure multi-party computation.

**Technology Stack**

*   **Python:** The primary programming language for implementing the federated learning algorithms, homomorphic encryption, and blockchain integration.
*   **TensorFlow/Keras:** Used for building and training machine learning models within the federated learning framework. Provides a high-level API for defining and training various neural network architectures.
*   **Ethereum (Private Blockchain):** Utilized for creating a decentralized, immutable ledger to record model updates, participant contributions, and training parameters. A private blockchain ensures control over the network and reduces transaction costs.
*   **Solidity:** The programming language used to write smart contracts that govern the blockchain interactions, manage access control, verify model updates, and distribute rewards.
*   **Web3.py:** A Python library for interacting with the Ethereum blockchain. Used to deploy and interact with smart contracts, retrieve data from the blockchain, and manage user accounts.
*   **Paillier Cryptosystem (Custom Implementation):** A custom implementation of the Paillier cryptosystem for homomorphic encryption. Optimized for performance and security in the context of federated learning.

**Installation**

1.  Clone the repository:
    git clone https://github.com/ezozu/CognitiveLedger.git
    cd CognitiveLedger

2.  Install Python dependencies:
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

3.  Install Ganache CLI (for running a local Ethereum blockchain):
    npm install -g ganache-cli

4.  Install Truffle (for compiling and deploying smart contracts):
    npm install -g truffle

5.  Start Ganache CLI:
    ganache-cli

6.  Compile and deploy smart contracts:
    truffle compile
    truffle migrate

**Configuration**

The following environment variables need to be configured:

*   `BLOCKCHAIN_ADDRESS`: The address of the Ethereum blockchain node (e.g., `http://localhost:8545`).
*   `CONTRACT_ADDRESS`: The address of the deployed smart contract.
*   `PRIVATE_KEY`: The private key of the Ethereum account used to interact with the smart contract.
*   `MODEL_SAVE_PATH`: The directory where the trained models will be saved.

These variables can be set in a `.env` file in the root directory of the project.

**Usage**

Example of training a federated learning model:

python3 federated_learning_client.py --blockchain_address <BLOCKCHAIN_ADDRESS> --contract_address <CONTRACT_ADDRESS> --private_key <PRIVATE_KEY> --model_save_path <MODEL_SAVE_PATH>

The `federated_learning_client.py` script handles the local model training, homomorphic encryption, and interaction with the blockchain. The script connects to the Ethereum blockchain, retrieves the current global model parameters from the smart contract, trains a local model on the client's data, encrypts the model updates using homomorphic encryption, and submits the encrypted updates to the smart contract. The smart contract then aggregates the encrypted updates, decrypts the aggregated updates, and updates the global model parameters.

For detailed API documentation, please refer to the docstrings within the Python code. Each module and function is thoroughly documented with explanations of its purpose, parameters, and return values.

**Contributing**

We welcome contributions to CognitiveLedger! Please follow these guidelines:

*   Fork the repository and create a branch for your feature or bug fix.
*   Write clear and concise commit messages.
*   Submit a pull request with a detailed description of your changes.
*   Ensure that your code adheres to the project's coding style.
*   Write unit tests for your code.

**License**

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ezozu/CognitiveLedger/blob/main/LICENSE) file for details.

**Acknowledgements**

We would like to thank the open-source community for providing valuable resources and tools that have made this project possible. Specifically, we acknowledge the contributions of the TensorFlow, Keras, and Web3.py communities.