import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import Login  from "./login/login";

export default function App() {
  return (
    <View style={styles.container}>
      <Login/>      
    </View>
  );
}
// #32465f - gray
// #5af0b9 - blue
// #798ca6 - gray text
const gray = '#32465f';
const blue = '#5af0b9';
const grayText = '#798ca6';
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
