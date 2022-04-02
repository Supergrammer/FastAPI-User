# Add GitHub Label

LABELS_DIR=".GitHub_Label"

ACCESS_TOKEN=$(<$LABELS_DIR/.accessToken)
REPOSITORY_NAME="Toy-Project-Template"

github-label-sync --access-token $ACCESS_TOKEN --labels $LABELS_DIR/labels.json Supergrammer/$REPOSITORY_NAME