from dulwich.object_store import PackBasedObjectStore


if hasattr(PackBasedObjectStore, 'delete_loose_object'):

    def delete_loose_object(object_store: PackBasedObjectStore, sha: bytes):
        object_store.delete_loose_object(sha)

else:

    def delete_loose_object(object_store: PackBasedObjectStore, sha: bytes):
        object_store._remove_loose_object(sha)
