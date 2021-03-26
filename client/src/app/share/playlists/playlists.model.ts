export default interface ResponsePlaylistData {
  api_available: { name: string; value: string }[];
  playlists: {
    api: string;
    created_at: string;
    is_active: boolean;
    playlist_id: string;
    record_id: string;
    user: string;
  }[];
  page: number;
  results: number;
}
