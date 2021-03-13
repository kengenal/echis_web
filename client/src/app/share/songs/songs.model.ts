export default interface ResponseSongsData {
  songs: {
    _id?: string;
    added_by: string;
    added_to_playlist: string;
    album: string;
    api: string;
    cover: string;
    created_at: string;
    is_shared: boolean;
    playlist_id?: string;
    rank: number;
    record_id?: string;
    song_id?: string;
    title: string;
  }[];
  page: number;
  results: number;
}
